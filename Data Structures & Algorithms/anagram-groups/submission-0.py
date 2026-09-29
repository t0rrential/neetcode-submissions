class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputList = []
        dictList = []

        for word in strs:
            nuDict = {}

            for letter in word:
                nuDict[letter] = nuDict.get(letter, 0) + 1

            if nuDict not in dictList:
                dictList.append(nuDict)

            anagramIndex = dictList.index(nuDict)
            
            if anagramIndex >= len(outputList):
                outputList.append([])

            outputList[anagramIndex].append(word)

        return outputList


                
