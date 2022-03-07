class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #rank each element
        rank_elements = sorted(set(arr))
        ranks = [i+1 for i in range(len(rank_elements))]
        rank_elements_map = dict(zip(rank_elements,ranks))
        return [rank_elements_map.get(ele) for ele in arr]
        