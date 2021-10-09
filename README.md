# CSV-Fixer

Short Program that would search for empty columns in data-sets we would receive and conditionally add the content of the line associated with the empty column to
the line above. The reason being is that the data-sets we would receive were in PDF format and had indentation within address columns. The conversion to CSV would cause error in our data format, as it would interpret indentations as new lines. 
