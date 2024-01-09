def add_data_json(json_file: str, hashTable: dict, console: object, samples: list):
    try:
        for sample in samples:
            index = hashTable.get(sample["Food_Name"])
            if index == None:
                index = len(json_file)
                json_file.append(sample)
                hashTable.update({sample["Food_Name"]: index})
            else:
                doc = json_file[index]
                doc = doc.update(sample)
                json_file[index] = doc
    except Exception as e:
        console.error(f"Exception while adding data in json list : {e}")
    return json_file, hashTable, ""


def scrap_table(soup: object, key: str, console):
    samples = list()
    try:
        table = soup.find("table", {"id": "ite"})
        tableHeaders = [
            tt.text.strip().replace("-", "_").encode("utf-8").decode()
            for tt in table.thead.tr.find_all("th")
        ]

        if key == "Amino_Acids":
            del tableHeaders[0]

        for data in table.tbody.find_all("tr"):
            temp = (
                data.text.split().replace(" ", "_").replace(",", "_").replace("__", "_")
            )

            if len(tableHeaders) != len(temp):
                td = data.find_all("td")
                td_text = [tt.text.strip() for tt in td]

            for text in td_text:
                if len(text) == 0:
                    index = td_text.index(text)
                    extracted_value = (
                        td[text]
                        .find("input", {"class": "text-button"})
                        .get("value")
                        .strip()
                        .replace(" ", "_")
                        .replace(",", "_")
                        .replace("__", "_")
                        .replace("(", "")
                        .replace(")", "")
                    )

                    temp.insert(index, extracted_value)

            # Adding into sample
            if len(tableHeaders) < 3:
                holder = {tableHeaders[0]: temp[0], tableHeaders[1]: temp[1]}
            else:
                holder = {
                    tableHeaders[0]: temp[0],
                    key: {k: v for k, v in zip(tableHeaders[1:], temp[1:])},
                }
            samples.append(holder)

    except Exception as e:
        console.error(f"Error while scrapping table for {key} : {e}")
        return f"Error while scrapping table for {key} : {e}"

    return samples, ""
