def reorderLogFiles(logs):
    def f(log):
        id_, rest = log.split(" ", 1)
        if rest[0].isalpha():
            return (0, rest, id_) 
        else:
            (1,)
    
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
reorderLogFiles(logs)