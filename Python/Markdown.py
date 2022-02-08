import re

"""Takes input from Exercism into and hooks it into MarkdownParse Class and returns the html_markdown object after it's done."""
def parse(markdown):
   return str(MarkdownParse(markdown).html_markdown)

class MarkdownParse():

    def __init__(self, markdown):
        """The passed markdown string is broken into newline strings in a list self.markdown"""
        self.markdown = markdown.split("\n")
        for index, line in enumerate(self.markdown):

            """Each newline item in the self.markdown list is separated into one of three types: header, item, or paragraph via regex. Defaults to paragraph if nothing else matches."""
            if re.match("^#+(.*)", line):
                line = self.header(line)
            elif re.match("(\*)(.*)", line):
                line = self.item(line)
            else:
                line = self.paragraph(line)

            """Each line is parsed for any bold or italic markings. First bold then italic as the italic regex expression can erroneously pick up the bold expression."""
            line = self.bold(line)
            line = self.italics(line)
            """Item in list is replaced by the transformed newline string"""
            self.markdown[index] = line

        """New parsed string is made from the final list by joining it together and then regex substituted to group items together into a singular list."""
        self.html_markdown = ''.join(self.markdown)
        self.html_markdown = re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", self.html_markdown)


    def paragraph(self, line):
        return f"<p>{line}</p>"

    def italics(self, line):
        return re.sub(r"_(.*)_", r"<em>\1</em>", line)
        
    def bold(self, line):
        return re.sub(r"__(.*)__", r"<strong>\1</strong>", line)
        
    def header(self, line):
        h_num = line.count("#", 0, 7)
        if h_num < 7:
            line = f"<h{h_num}>{line[h_num+1:]}</h{h_num}>"
            return line
        else:
            return self.paragraph(line)

    def item(self, line):
        return f"<li>{line[2:]}</li>"