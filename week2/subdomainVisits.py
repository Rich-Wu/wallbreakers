from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for entry in cpdomains:
            entry = entry.split(" ")
            entry[1] = entry[1].split(".")
            domain_name = entry[1][-1]
            counter[domain_name] += int(entry[0])
            for domain in entry[1][-2::-1]:
                domain_name = domain + '.' + domain_name
                counter[domain_name] += int(entry[0])
        ans = []
        for key in counter:
            ans.append("{0} {1}".format(counter[key], key))
        return ans
