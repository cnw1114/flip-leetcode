class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashT = {}
        for elem in cpdomains:
            count, domain = elem.split(' ')
            if domain not in hashT:
                hashT[domain] = int(count)
            else:
                hashT[domain] += int(count)
            if '.' in domain:
                while True:
                    dotidx=domain.find('.')
                    if dotidx<0:break
                    domain = domain[dotidx+1:]
                    if domain not in hashT:
                        hashT[domain] = int(count)
                    else:
                        hashT[domain] += int(count)
            
        return [str(value)+' '+key for key, value in hashT.items()]
                    
        
