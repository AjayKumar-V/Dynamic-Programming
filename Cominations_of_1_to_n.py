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

print()
print(Solution.combinations(None,4,2))