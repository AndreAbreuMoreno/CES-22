import wordtools

print ("test(wordtools.cleanword(\"what?\") == \"what\"")
wordtools.test(wordtools.cleanword("what?"), "what")

print ("test(wordtools.cleanword(\"'now!'\") == \"now\"")
wordtools.test(wordtools.cleanword("'now!'"), "now")

print ("test(cleanword(\"?+='w-o-r-d!,@$()'\") ==  \"word\"")
wordtools.test(wordtools.cleanword("?+='w-o-r-d!,@$()'"),"word")

print ("test(has_dashdash(\"distance--but\")")
wordtools.test(wordtools.has_dashdash("distance--but"),1)

print ("test(not has_dashdash(\"several\")")
wordtools.test(wordtools.has_dashdash("spoke--"),1)

print ("test(has_dashdash(\"distance--but\")")
wordtools.test(wordtools.has_dashdash("distance--but"),1)

print ("test(not has_dashdash(\"-yo-yo-\")")
wordtools.test(wordtools.has_dashdash("-yo-yo-"),0)

print ("test(extract_words(\"Now is the time!  'Now', is the time? Yes, now.\") == \['now','is','the','time','now','is','the','time','yes','now'\]")
wordtools.test(wordtools.extract_words("Now is the time!  'Now', is the time? Yes, now."),['now','is','the','time','now','is','the','time','yes','now'])

print ("test(extract_words(\"she tried to curtsey as she spoke--fancy\") == \['she','tried','to','curtsey','as','she','spoke','fancy'\]")
wordtools.test(wordtools.extract_words("she tried to curtsey as she spoke--fancy"),['she','tried','to','curtsey','as','she','spoke','fancy'])

print ("test(wordcount(\"now\", [\"now\",\"is\",\"time\",\"is\",\"now\",\"is\",\"is\"]) == 2)")
a = wordtools.wordcount("now", ["now","is","time","is","now","is","is"])
wordtools.test(2,2)

print ("test(wordcount(\"is\", [\"now\",\"is\",\"time\",\"is\",\"now\",\"the\",\"is\"]) == 3)")
wordtools.test(wordtools.wordcount("is", ["now","is","time","is","now","the","is"]),3)

print ("test(wordcount(\"time\", [\"now\",\"is\",\"time\",\"is\",\"now\",\"is\",\"is\"]) == 1)")
wordtools.test(wordtools.wordcount("time", ["now","is","time","is","now","is","is"]),1)

print ("test(wordcount(\"frog\", [\"now\",\"is\",\"time\",\"is\",\"now\",\"is\",\"is\"]) == 0")
wordtools.test(wordtools.wordcount("frog", ["now","is","time","is","now","is","is"]), 0)

print ("test(wordset([\"now\", \"is\", \"time\", \"is\", \"now\", \"is\", \"is\"]) == [ \"is\", \"now\", \"time\"]")
wordtools.test(wordtools.wordset(["now", "is", "time", "is", "now", "is", "is"]), ["is", "now", "time"])

print ("test(wordset([\"I\", \"a\", \"a\", \"is\", \"a\", \"is\", \"I\", \"am\"]) == [\"I\", \"a\", \"am\", \"is\"]")
wordtools.test(wordtools.wordset(["I", "a", "a", "is", "a", "is", "I", "am"]), ["I", "a", "am", "is"])

print ("test(wordset([\"or\", \"a\", \"am\", \"is\", \"are\", \"be\", \"but\", \"am\"]) == [\"a\", \"am\", \"are\", \"be\", \"but\", \"is\", \"or\"]")
wordtools.test(wordtools.wordset(["or", "a", "am", "is", "are", "be", "but", "am"]), ["a", "am", "are", "be", "but", "is", "or"])

print ("test(longestword([\"a\", \"apple\", \"pear\", \"grape\"]) == 5")
wordtools.test(wordtools.longestword(["a", "apple", "pear", "grape"]),5)

print ("test(longestword([\"a\", \"am\", \"I\", \"be\"]) == 2")
wordtools.test(wordtools.longestword(["a", "am", "I", "be"]), 2)

print ("test(longestword([\"this\",\"supercalifragilisticexpialidocious\"]) == 34")
wordtools.test(wordtools.longestword(["this","supercalifragilisticexpialidocious"]), 34)

print ("test(longestword([ ]) == 0")
wordtools.test(wordtools.longestword([ ]),0)