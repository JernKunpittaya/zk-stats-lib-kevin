
# just for testing simple code stuffs
import numpy as np

# generate data for 1 col
# array = np.floor(np.random.uniform(1,100, 50))
array = np.round(np.random.normal(5000, 200,1000), 0)

print(", ".join(map(str, array)))

# print(len([9.8, 43.0, 89.2, 40.0, 46.8, 1.5, 33.7, 14.3, 42.3, 37.7, 94.2, 42.1, 70.3, 73.7, 18.1, 80.8, 61.8, 44.1, 4.9, 8.3, 71.5, 52.2, 20.7, 27.5, 75.0, 6.1, 97.8, 63.7, 45.8, 62.2, 18.8, 92.2, 74.7, 37.4, 79.8, 85.6, 97.4, 99.9, 21.1, 100.0, 34.9, 41.5, 23.3, 77.1, 29.6, 58.8, 23.3, 65.8, 10.7, 56.6, 80.2, 23.5, 11.8, 6.2, 29.2, 51.1, 11.9, 14.7, 2.2, 43.0, 13.3, 80.9, 51.9, 95.6, 26.1, 1.3, 34.5, 74.0, 22.9, 62.1, 54.3, 3.5, 95.0, 4.0, 53.5, 71.2, 5.6, 18.5, 43.0, 62.2, 16.6, 13.0, 71.9, 3.7, 99.7, 79.2, 83.7, 81.3, 14.8, 46.3, 22.6, 56.6, 8.6, 40.3, 56.3, 59.6, 97.6, 65.4, 74.7, 11.4, 90.4, 81.4, 33.9, 37.5, 17.9, 68.0, 71.1, 61.6, 13.6, 47.2, 68.5, 99.1, 31.8, 4.6, 48.3, 93.2, 38.4, 92.8, 2.9, 59.8, 86.4, 35.9, 84.1, 83.7, 55.7, 25.5, 33.5, 70.8, 3.3, 50.0, 71.4, 44.2, 83.8, 40.7, 72.9, 44.3, 25.6, 49.4, 21.1, 32.5, 75.4, 89.2, 65.1, 36.4, 91.6, 79.5, 16.0, 78.5, 22.5, 50.2, 33.5, 20.8, 63.1, 31.2, 92.5, 55.2, 43.4, 1.7, 84.2, 38.8, 80.9, 67.2, 43.8, 13.1, 32.2, 31.9, 18.3, 19.5, 45.6, 43.1, 67.1, 66.2, 67.5, 66.2, 6.9, 1.3, 64.6, 27.7, 45.5, 56.4, 19.3, 35.4, 32.5, 47.3, 62.0, 80.2, 7.5, 48.3, 53.8, 86.9, 52.7, 77.5, 43.6, 24.8, 93.6, 27.1, 29.1, 87.5, 14.8, 71.3, 66.2, 94.7, 18.5, 53.1, 40.0, 71.8, 94.7, 35.0, 93.2, 38.3, 56.6, 82.3, 4.0, 6.8, 72.4, 73.1, 18.1, 93.7, 40.6, 89.8, 50.0, 61.1, 73.9, 20.6, 91.3, 37.0, 60.4, 89.8, 72.7, 37.9, 2.8, 40.6, 41.5, 59.2, 63.9, 32.4, 78.0, 57.2, 33.2, 66.1, 44.7, 45.8, 22.9, 43.7, 73.1, 99.7, 11.3, 47.3, 32.1, 6.8, 13.8, 7.7, 24.6, 71.9, 39.8, 1.9, 83.2, 12.9, 25.3, 32.3, 12.3, 54.9, 81.1, 23.7, 81.7, 89.0, 9.4, 42.5, 29.3, 24.8, 23.9, 22.3, 36.9, 59.8, 34.6, 62.3, 63.0, 11.0, 24.4, 6.2, 50.9, 75.9, 2.4, 59.9, 94.5, 13.5, 68.8, 53.4, 78.6, 4.3, 45.8, 67.0, 59.2, 16.6, 5.7, 75.5, 38.7, 98.0, 52.1, 33.7, 66.8, 27.2, 27.6, 46.3, 58.7, 19.5, 62.4, 49.3, 32.4, 67.5, 96.0, 57.2, 84.9, 14.1, 9.0, 51.0, 32.1, 89.0, 82.8, 81.6, 10.1, 32.9, 48.3, 18.4, 47.6, 98.3, 55.2, 50.8, 57.1, 37.9, 97.0, 8.0, 45.1, 78.0, 90.6, 37.1, 84.3, 73.6, 25.4, 37.3, 99.7, 32.2, 61.2, 96.8, 58.3, 89.9, 15.8, 2.2, 68.9, 24.9, 93.8, 16.5, 47.3, 89.1, 70.8, 38.8, 95.2, 94.4, 74.6, 11.1, 28.2, 66.7, 67.3, 99.8, 45.7, 1.4, 80.2, 79.6, 81.5, 99.1, 59.3, 45.0, 4.0, 99.0, 67.9, 77.4, 82.3, 87.2, 43.1, 23.6, 69.3, 97.4, 82.8, 30.7, 20.7, 21.3, 63.8, 71.3, 2.8, 43.1, 53.9, 72.9, 82.8, 36.7, 59.8, 20.4, 26.8, 86.3, 81.2, 3.6, 11.6, 48.2, 11.3, 43.7, 6.0, 24.5, 62.1, 74.7, 82.5, 69.1, 20.2, 2.6, 16.3, 4.9, 2.9, 58.6, 87.1, 2.2, 11.0, 51.7, 60.9, 67.9, 42.0, 15.8, 47.7, 16.3, 45.4, 23.2, 81.3, 44.3, 53.4, 29.4, 11.9, 97.4, 57.5, 36.3, 8.3, 53.5, 31.2, 15.5, 10.2, 18.3, 92.9, 41.0, 92.0, 73.8, 80.4, 46.1, 65.7, 99.4, 12.9, 70.9, 82.2, 13.7, 65.7, 91.4, 94.6, 1.1, 86.4, 32.4, 52.2, 62.2, 3.5, 87.7, 11.3, 51.9, 11.3, 50.9, 10.5, 47.4, 66.7, 64.1, 49.8, 93.3, 69.7, 50.6, 71.2, 35.9, 16.1, 93.3, 37.1, 24.2, 86.0, 94.6, 80.9, 47.4, 55.1, 85.4, 78.1, 90.4, 79.2, 29.0, 27.8, 40.5, 42.2, 68.6, 59.7, 40.4, 61.2, 62.0, 69.1, 47.9, 1.9, 45.7, 49.5, 31.9, 94.7, 35.7, 89.8, 49.2, 84.4, 37.5, 83.3, 94.7, 49.9, 58.4, 88.9, 69.4, 61.9, 7.5, 96.9, 89.4, 55.5, 68.7, 78.0, 77.5, 43.3, 51.3, 80.1, 35.5, 41.6, 31.9, 15.4, 69.2, 29.7, 17.0, 31.5, 15.8, 41.7, 71.8, 10.2, 95.6, 17.1, 14.5, 22.0, 62.6, 45.6, 43.4, 78.6, 46.0, 86.4, 3.8, 56.0, 55.5, 99.8, 78.2, 14.5, 66.4, 45.9, 52.9, 91.7, 61.3, 25.7, 80.6, 80.8, 55.6, 47.7, 42.2, 97.8, 90.3, 17.7, 60.5, 82.0, 74.8, 92.6, 70.5, 31.3, 45.5, 78.4, 66.0, 19.8, 54.3, 92.8, 95.3, 6.9, 54.2, 15.2, 88.6, 77.1, 77.7, 19.1, 51.6, 56.4, 47.9, 6.1, 65.9, 69.7, 62.1, 68.4, 2.1, 75.1, 33.1, 80.6, 56.6, 84.1, 79.8, 42.1, 46.2, 15.7, 17.1, 90.9, 23.0, 90.9, 18.0, 38.6, 82.4, 4.0, 9.4, 68.6, 96.8, 84.7, 17.1, 53.4, 45.7, 59.8, 26.8, 52.7, 23.6, 92.0, 68.1, 70.3, 4.0, 89.2, 36.0, 85.5, 56.5, 3.6, 14.1, 69.4, 35.7, 39.9, 43.9, 98.2, 54.3, 1.8, 26.4, 95.9, 78.6, 64.3, 8.9, 6.5, 55.5, 67.6, 74.8, 78.0, 45.3, 14.7, 54.0, 32.8, 85.8, 53.3, 4.8, 92.7, 36.6, 54.5, 72.7, 74.7, 98.8, 1.6, 46.6, 9.4, 12.2, 98.7, 44.4, 84.9, 7.2, 11.5, 11.0, 35.1, 18.5, 40.4, 24.8, 1.2, 81.8, 60.3, 21.5, 87.1, 23.6, 88.2, 20.2, 2.5, 67.6, 17.2, 28.1, 56.2, 61.8, 94.6, 61.0, 46.8, 20.2, 65.5, 7.2, 20.9, 40.5, 39.8, 50.2, 31.1, 16.1, 5.6, 11.4, 25.9, 97.3, 19.9, 79.2, 86.0, 86.1, 10.1, 74.5, 76.8, 46.3, 80.6, 6.6, 23.6, 43.3, 52.0, 19.7, 59.6, 9.7, 18.5, 83.6, 90.6, 32.1, 10.4, 8.3, 88.0, 67.4, 52.8, 56.7, 80.1, 93.3, 75.5, 79.0, 96.7, 53.4, 69.2, 83.6, 99.7, 4.0, 79.8, 98.8, 19.8, 91.6, 13.3, 19.4, 96.2, 97.5, 78.9, 58.6, 20.5, 22.6, 93.0, 23.9, 57.6, 25.9, 75.8, 54.1, 50.3, 89.7, 88.5, 72.2, 2.3, 6.7, 83.8, 15.2, 83.3, 51.4, 86.9, 23.5, 39.6, 24.6, 79.1, 97.5, 31.5, 91.6, 7.8, 91.4, 69.3, 11.2, 99.9, 34.2, 35.1, 6.5, 35.4, 67.5, 52.9, 100.0, 65.2, 68.1, 18.9, 16.3, 45.7, 22.5, 15.2, 21.7, 71.6, 97.2, 53.0, 85.5, 75.9, 90.6, 21.0, 94.6, 31.7, 18.4, 67.1, 39.6, 4.2, 52.6, 80.5, 98.7, 33.5, 78.7, 8.9, 2.5, 54.5, 80.8, 88.8, 63.5, 99.8, 68.1, 66.0, 71.4, 53.3, 93.0, 83.2, 34.4, 96.2, 30.7, 91.1, 80.1, 87.8, 1.6, 2.7, 59.1, 65.9, 21.1, 96.9, 23.4, 96.0, 18.6, 83.0, 95.8, 70.4, 19.3, 17.1, 9.5, 1.3, 11.0, 21.2, 78.2, 89.0, 71.2, 37.7, 46.6, 88.8, 91.1, 37.7, 19.9, 53.7, 9.4, 93.2, 99.3, 33.4, 82.0, 35.5, 55.8, 35.0, 91.2, 41.6, 48.7, 61.7, 58.9, 69.8, 19.7, 36.8, 12.0, 72.5, 88.0, 33.1, 86.2, 2.9, 66.4, 6.2, 8.5, 68.4, 31.3, 68.3, 15.6, 45.5, 8.3, 54.7, 85.2, 6.4, 40.4, 87.3, 19.2, 95.3, 60.5, 26.2, 38.4, 85.0, 53.2, 92.0, 72.5, 52.3, 73.0, 82.8, 97.1, 18.5, 84.1, 86.8, 4.6, 76.1, 28.3, 85.9, 58.1, 37.6, 22.4, 18.0, 89.9, 71.9, 88.0, 57.7, 76.8, 47.9, 91.1, 60.5, 11.9, 22.1, 79.7, 75.6, 28.7, 91.0, 85.0, 65.8, 27.7, 97.5, 66.7, 87.9, 96.4, 1.6, 100.0, 93.1, 83.1, 68.9, 79.7, 84.9, 25.2, 39.0, 10.6, 58.5, 48.2, 41.6, 86.1, 83.7, 51.6, 62.3, 54.6, 83.5, 50.8, 61.4, 3.3, 48.5, 15.1, 46.9, 61.9, 58.7, 14.1, 5.2, 15.1, 10.2, 19.8, 43.9, 45.5, 44.0, 24.6, 92.5, 30.7, 63.8, 27.3, 67.3, 8.5, 97.3, 7.7, 37.5, 58.7, 39.1, 49.3, 86.2, 62.2]))