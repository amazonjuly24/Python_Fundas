import pandas as pd
import graphlab

r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']


ratings = pd.read_csv('movielens/rate.csv', sep='\t', names=r_cols,
 encoding='latin-1')

print "\nRATINGS:"
print ratings.shape
print ratings.head()


r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings_base = pd.read_csv('movielens/train.csv', sep='\t', names=r_cols, encoding='latin-1')

ratings_test = pd.read_csv('movielens/test.csv', sep='\t', names=r_cols, encoding='latin-1')

print ratings_base.shape, ratings_test.shape

train_data = graphlab.SFrame(ratings_base)
test_data = graphlab.SFrame(ratings_test)

popularity_model = graphlab.popularity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating')

print(popularity_model)

popularity_recomm = popularity_model.recommend(users=range(1,6),k=5)
popularity_recomm.print_rows(num_rows=25)

#print(popularity_recomm)

print ratings_base.groupby(by='movie_id')['rating'].mean().sort_values(ascending=False).head(10)

item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='pearson')

item_sim_recomm = item_sim_model.recommend(users=range(1,6),k=5)
#print(item_sim_recomm)
item_sim_recomm.print_rows(num_rows=25)
print("\n------------MODEL PERFORMANCE--------------------------------------\n")
model_performance = graphlab.compare(test_data, [popularity_model, item_sim_model])
print(model_performance)
