# Index Maker 
<p> Tool used to create an index from a spreadsheet. </p>
<h2> Background </h2>
<p> Developed this tool to create an index for the SEC275.1, SEC275.2 and SEC275.3 textbooks while studying for the GIAC Foundational Cybersecurity Technologies (GFACT) certification exam. </p>
<h2> Usage </h2>
<p> Create a spreadsheet with these 4 columns: 
  
| Title  | Description | Pages | Books |
| ------------- | ------------- | ------------- | ------------- |
| Name of term  | Description of term | Pages in which it is found | Book in which is it found |

</p>

### Steps

<p>
  
1. Ensure that there are no commas in any of the columns, as this tool used the commas to parse the input file. 
2. Download the spreadsheet as a .csv file (comma separated values).
3. Delete the first line in the file (the headers), copy the contents, and paste the contents into the input.txt file under the input folder.
4. Under the src folder, open the indexmaker.py file and run it.
5. The output will be in the output folder, in output.html.
6. Open that output.html file in a web browser. 

Additional Steps for Formatting:
  *  Copy the contents displayed in the web browser into a google doc
  *  Change the google doc to 3 columns
  *  Play around with the font and sizes
  *  Consider adding a title
  *  Consider adding additional description for different tools at the end

</p>
