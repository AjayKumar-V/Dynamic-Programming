class Solution:
	def combinations(self,n, r):
		res = [ ]

		def backtrack(start, comb):
			if len(comb) == r:
				res.append(comb.copy( ))
				return
			
			for i in range(start, n+1):
				#print(comb, res)
				comb.append(i)
				backtrack(i+1, comb)
				comb.pop( )
		backtrack(1, [ ])
		
		return res


n = int(input())
r = int(input())
# Printing combinations of size r from numbers 1 to n.
print(Solution.combinations(None,n,r))
