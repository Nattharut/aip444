# chunker.py
import re

# Remove HTML comments, which Node docs use for metadata
def clean_markdown(text):
    return re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()

def chunk_markdown(text, source):
    lines = clean_markdown(text).split('\n')
    chunks = []

    current_heading = 'Introduction'
    # We keep a stack of headings to build breadcrumbs (e.g. fs > readFile)
    breadcrumbs = [current_heading]
    current_content = []
    chunk_counter = 0
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        # Detect headings (only if not in code block)
        heading_match = None
        if not in_code_block:
            heading_match = re.match(r'^(#{1,6})\s+(.*)', line)

        if heading_match:
            # 1. Save the previous section as a chunk
            if current_content:
                content = '\n'.join(current_content).strip()
                # Skip empty or very short sections
                if len(content) > 50:
                    chunks.append({
                        'id': f"{source}-{chunk_counter}",
                        # Inject breadcrumbs into content, for better embedding
                        'content': f"{' > '.join(breadcrumbs)}\n\n{content}",
                        'metadata': {
                            'source': source,
                            'heading': current_heading,
                            'breadcrumb': ' > '.join(breadcrumbs)
                        }
                    })
                    chunk_counter += 1

            # 2. Update state for new section
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            current_heading = title

            # Update breadcrumb stack based on heading level
            if len(breadcrumbs) < level:
                breadcrumbs.append(title)
            else:
                breadcrumbs = breadcrumbs[:level-1] + [title]

            current_content = []
        else:
            current_content.append(line)

    # Final chunk
    if current_content:
        final_content = '\n'.join(current_content).strip()
        chunks.append({
            'id': f"{source}-{chunk_counter}",
            'content': f"{' > '.join(breadcrumbs)}\n\n{final_content}",
            'metadata': {
                'source': source,
                'heading': current_heading,
                'breadcrumb': ' > '.join(breadcrumbs)
            }
        })
    return chunks
