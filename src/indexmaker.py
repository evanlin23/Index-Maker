with open("input/input.txt") as file:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Parsing input file
    # Ensure that there are no commas in the spreadsheet beforehand 
    # Download spreadsheet as comma separated values
    # Spreadsheet must have these 4 columns, in order:
    # Title    Description    Page    Book

    content = file.read()
    rows1 = content.split("\n")
    rows2 = []
    for i in range(len(rows1)):
        x = rows1[i].split(",")
        rows2.append(x)
    rows3 = sorted(rows2,key=lambda x: x[0].title())

    # Creating output html file
    string1 = "<!doctype html>\n"
    string1 += "  <html>\n"
    string1 += "    <body>\n"
    string1 += "      <span style='font-size: 42px'>"

    # Manually creating section for all non-letter terms
    string1 += "##"
    string1 += "</span>"
    string1 += "<br/>\n"
    lastLetter = "#"

    for i in range(len(rows3)):
        # Find when the first letter changes and where we need to add a heading 
        if ((rows3[i][0][0].lower() != lastLetter.lower()) and rows3[i][0][0].lower() in alphabet):
            string1 += "      <span style='font-size: 42px'>"
            string1 += rows3[i][0][0] + rows3[i][0][0].lower()
            string1 += "</span>"
            string1 += "<br/>\n"
            string1 += "      <span style='font-size: 1.5px'>"
            string1 += "————————————————————————————————————————————————————————————————"
            string1 += "</span>"
            string1 += "<br/>\n"
            lastLetter = rows3[i][0][0]
        
        # Formatting index entry as 
        #   Name [books,pages] definition

        string1 += "        <b style='color:blue;'>" + rows3[i][0] + "</b>" + " <i>[b" + rows3[i][3] + ",p" + rows3[i][2] + "]</i> "
        string1 += rows3[i][1] + "<br/>\n"
        
    string1 += "    </body>\n"
    string1 += "  </html>"

    with open("output/output.html", "w") as file2:
        file2.write(string1)

