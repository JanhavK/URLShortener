# We are going to make a url shortener with unique ids for each unqiue url
class urlshortener:
        # This dict stores the urls which we have already shortened
        urldict = {}
        # We want to start at 1 for the first url
        id = 1
        def shorturl(self, longurl):
                # This if condition checks to see if we already have the url in our dict
                if longurl in self.urldict:
                        id = self.urldict[longurl]
                        shorturl = self.encode(id)
                else:
                        # We now store the unique url in our dict
                        self.urldict[longurl] = self.id
                        shorturl = self.encode(self.id)
                        # We increase the id so that the next unique url will have a unique id of it's own
                        self.id += 1
                return "shortened.com/"+shorturl

        def encode(self, id):
                # We now allow the unique id to be base 62 rather than just base 10
                characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                newbase = len(characters)
                finalid = []
                # We now convert the previously base 10 to base 62
                while id > 0:
                    num = id % newbase
                    finalid.append(characters[num])
                    id = id // newbase
                # Since our finalid is already reversed we need to once again reverse it to return the value
                return "".join(finalid[::-1])
		
def main():
        shorten = urlshortener()
        url = ""
        # We now define an exit and can make an input for users to input their own website to be shortened
        while url != "end":
                url = input("Input a url. Type 'end' to end the program:\n")
                if url == "end":
                        continue
                else:
                        print(shorten.shorturl(url))
                        print()

main()
