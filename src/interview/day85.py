class Solution:
  def compareVersion(self, version1, version2):
    ver1 = list(map(int, version1.split('.')))
    ver2 = list(map(int, version2.split('.')))
    if len(ver2) > len(ver1):
        return self.compareVersion(version2, version1)
    for _ in range(len(ver1)-len(ver2)):
        ver2.append(0)
    for i in range(len(ver1)):
        if ver1[i] > ver2[i]:
            return 1
        elif ver1[i] == ver2[i]:
            continue
        else:
            return -1
    return 0

version1 = "1.0.1"
version2 = "1.0.002"
print(Solution().compareVersion(version1, version2))
# 1