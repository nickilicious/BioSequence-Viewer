# ChatGPT, Claude AI and Github copilot assisted with the implementation of these functions

def parse_aln(file):
    sequences = []

    for line in file:
        # Decode line from bytes to utf-8 string
        line = line.decode('utf-8')

        if line.startswith(">"):
            # Split the line at the first space
            name_parts = line[1:].strip().split()
            name = name_parts[0]
            sequences.append({"name": name, "seq": ""})
        else:
            # Add sequence to the last entry in sequences
            sequences[-1]["seq"] += line.strip()

    return sequences


def parse_clw(file):
    sequences = []

    for line in file:
        # Decode line from bytes to utf-8 string
        line = line.decode('utf-8')
        if line.startswith("CLUSTAL"):
            continue

        # Split the line at whitespace
        line_parts = line.strip().split()

        if len(line_parts) >= 2:
            name = line_parts[0]
            sequence = line_parts[1]

            # Check if the line contains sequence information
            if name and sequence and "*" not in name:
                # Find or create the sequence entry
                seq_entry = next((seq for seq in sequences if seq["name"] == name), None)
                if not seq_entry:
                    seq_entry = {"name": name, "seq": ""}
                    sequences.append(seq_entry)

                seq_entry["seq"] += sequence

    return sequences

def parse_fst(file):
    sequences = []

    for line in file:
        # Decode line from bytes to utf-8 string
        line = line.decode('utf-8')

        if line.startswith(">"):
            # Split the line at the first space
            name_parts = line[1:].strip().split()
            name = name_parts[0]
            sequences.append({"name": name, "seq": []})
        else:
            sequences[-1]["seq"].append(line.strip())

    for seq in sequences:
        seq["seq"] = "".join(seq["seq"])

    return sequences
