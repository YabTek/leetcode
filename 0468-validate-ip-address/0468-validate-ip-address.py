class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(cur):
            div = cur.split('.')
            if len(div) != 4:
                return False
            for part in div:
                if not part.isdigit() or not (0 <= int(part) <= 255) or (len(part) > 1 and part[0] == '0'):
                    return False
            return True
    
        def isIPv6(cur):
            div = cur.split(':')
            if len(div) != 8:
                return False
            for part in div:
                if not (1 <= len(part) <= 4) or not all(c.isdigit() or 'a' <= c <= 'f' or 'A' <= c <= 'F' for c in part):
                    return False
            return True

        if '.' in queryIP and isIPv4(queryIP):
            return "IPv4"
        elif ':' in queryIP and isIPv6(queryIP):
            return "IPv6"
        return "Neither"


