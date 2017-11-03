import numpy as np
import pandas as pd


def binary_matrix_popular_items(data):
    """
    :params data: df | this is the input data that should be sampled
    
    returns a ratings matrix with the hit rates of the 100 most popular items
    """
    
    # get items by popularity
    media_count = data.groupby('media_id')['user_id'].nunique()
    media_count = media_count.sort_values(axis=0, ascending=False)
    
    # Select top 100 items
    media = media_count[:100].index
    
    #filter data
    matrix = data[data['media_id'].isin(media)]
    
    # make pivot table
    matrix = matrix.pivot_table(index='user_id', columns='media_id',
                                values='is_listened', aggfunc='median')
    # filter users with less than 10 ratings in items
    m = matrix.count(axis=1) > 10
    matrix = matrix[matrix.index.isin(m[m==True].index)]
    matrix = matrix.applymap(round)
    
    return matrix


def binary_matrix_50_50(data):
    """
    :params data: df | this is the input data that should be sampled
    
    returns a ratings matrix with the hit rates of the 50 most
    popular items and the 50 random sampled items from the next 10,000 items.
    """
    # get items by popularity
    media_count = data.groupby('media_id')['user_id'].nunique()
    media_count = media_count.sort_values(axis=0, ascending=False)
    
    # Select top 50/50 items
    media1 = media_count[:50]
    media2 = media_count[51:10000].sample(n=50)
    media = media1.append(media2).index
    
    #filter data
    matrix = data[data['media_id'].isin(media)]
    
    # make pivot table
    matrix = matrix.pivot_table(index='user_id', columns='media_id',
                                values='is_listened', aggfunc='median')
    # filter users with less than 10 ratings in items
    m = matrix.count(axis=1) > 10
    matrix = matrix[matrix.index.isin(m[m==True].index)]
    # Round the values to avoid media = 0.5
    matrix = matrix.applymap(round)
    
    return matrix


def hit_rate_matrix_popular_items(data):
    """
    :params data: df | this is the input data that should be sampled
    
    returns a ratings matrix with the hit rates of the 100 most popular items
    """
    
    # get items by popularity
    media_count = data.groupby('media_id')['user_id'].nunique()
    media_count = media_count.sort_values(axis=0, ascending=False)
    
    # Select top 100 items
    media = media_count[:100].index
    
    #filter data
    matrix = data[data['media_id'].isin(media)]
    
    # make pivot table
    matrix = matrix.pivot_table(index='user_id', columns='media_id',
                                values='is_listened', aggfunc='mean')
    # filter users with less than 10 ratings in items
    m = matrix.count(axis=1) > 10
    matrix = matrix[matrix.index.isin(m[m==True].index)]
    
    return matrix


def hit_rate_matrix_50_50(data):
    """
    :params data: df | this is the input data that should be sampled
    
    returns a ratings matrix with the hit rates of the 50 most popular
    items and the 50 random sampled items from the next 10,000 items.
    """
    # get items by popularity
    media_count = data.groupby('media_id')['user_id'].nunique()
    media_count = media_count.sort_values(axis=0, ascending=False)
    
    # Select top 50/50 items
    media1 = media_count[:50]
    media2 = media_count[51:10000].sample(n=50)
    media = media1.append(media2).index
    
    #filter data
    matrix = data[data['media_id'].isin(media)]
    
    # make pivot table
    matrix = matrix.pivot_table(index='user_id', columns='media_id',
                                values='is_listened', aggfunc='mean')
    # filter users with less than 10 ratings in items
    m = matrix.count(axis=1) > 10
    matrix = matrix[matrix.index.isin(m[m==True].index)]
    
    return matrix
