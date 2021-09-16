<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>This is simple python program that reads a csv file using pandas library</strong></p>
<ul style="list-style-type: disc;">
    <li>Create an environment &amp; Install dependencies found in the .py files using pip in the command prompt.</li>
    <li>Run the file in the command prompt - run.bat</li>
    <li>Application</li>
</ul>
<ul style="list-style-type: disc;margin-left:0.25in;">
    <li>Part 1<ol style="list-style-type: circle;">
            <li>Downloads the csv data file at https://gist.github.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2 as &quot;raw&quot; and reads the file into a program memory.</li>
            <li>Once the data is read into memory it prints out how many rows of the data is in the CSV data.</li>
            <li>Then it removes all the rows in memory with &apos;profit&apos; that are not a numerical value.</li>
            <li>Then it prints out how many rows of data are left in memory, after removing all the rows with invalid non-numeric profit column data.&nbsp;</li>
        </ol>
    </li>
    <li>Part 2<ol style="list-style-type: circle;">
            <li>Converts the contents read into memory into JSON format and writes it out to a file called data2.json which only contains rows of data that have the valid numeric profit values. Each row in the Array contains data columns like year, rank, company, revenue, and profit.</li>
            <li>Orders the data in memory based on the profit value.</li>
            <li>Prints the top 20 rows in memory with the highest profit values&nbsp;</li>
        </ol>
    </li>
    <li>Part 3<ol style="list-style-type: circle;">
            <li>A file called data2.json is produced.</li>
        </ol>
    </li>
</ul>

