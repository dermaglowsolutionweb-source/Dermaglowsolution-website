def delete_diode_pico():
    # Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('<!-- Category: Diode + Pico Laser -->')
    if start_idx != -1:
        end_idx = content.find('<!-- Category 1: Premium Hydra Machines -->', start_idx)
        if end_idx != -1:
            content = content[:start_idx] + content[end_idx:]
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Successfully removed from index.html")
        else:
            print("Could not find end of Diode + Pico section")
    else:
        print("Could not find start of Diode + Pico section")

    # Update admin.js
    with open('admin/admin.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if "'Diode + Pico Laser'" not in line:
            new_lines.append(line)
            
    with open('admin/admin.js', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully removed from admin.js")

if __name__ == '__main__':
    delete_diode_pico()
