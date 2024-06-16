
# data đầu vào
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]

# data cần vectorize
input_str = "Tôi thích AI thích Toán"

# tách danh sách
def standardlize(data):
    data = " ".join(data) # Nối câu thành 1 câu đơn
    data = set(word for sentence in corpus for word in sentence.split()) # Từ câu đơn tách ra từ đơn
    data = sorted(list(data)) # sắp xếp từ đơn theo thứ tự tăng dần
    return data

corpus_list = standardlize(corpus)

vector = [0] * len(corpus_list) # tạo list vector trống với độ dài corpus
for word in input_str.split():
    if word in corpus_list: # so sánh
        vector[corpus_list.index(word)] += 1

print(f"Bag-of-Words: {corpus_list}")
print(f"{input_str}: {vector}")