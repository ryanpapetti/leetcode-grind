class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        #first let's only get the vegan restaurants if necessary
        if veganFriendly:
            restaurants = [restaurant for restaurant in restaurants if restaurant[2]]
        
        #now only get things in the relevant fields
        restaurants = [restaurant for restaurant in restaurants if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance]
        
        #NOW sort 
        
        restaurants.sort(key=lambda x: x[1], reverse = True)
        
        #now i have to check to make sure that the indices are in order
        
        sorted_all_ratings = sorted(set([restaurant[1] for restaurant in restaurants]))[::-1]
        
        final_ids = []
        
        for rating in sorted_all_ratings:
            sorted_by_id = sorted([restaurant[0] for restaurant in restaurants if restaurant[1] == rating])[::-1]
            final_ids.extend(sorted_by_id)
        
        return final_ids
        