import os
import random
from PIL import Image
import io
import base64
import image_search_pb2, image_search_pb2_grpc

import grpc
from concurrent import futures
# server/image_database/cat
ROOT_DIR = "/home/minhaz/UTA/DS/project-2/grpc-search/server/image_database"

def search_files(keyword):
    search_directory = os.path.join(ROOT_DIR, keyword)
    result_paths = os.listdir(search_directory)
    RANDOM_LOC = random.randint(0,1)
    selected_res =  os.path.join(search_directory, result_paths[RANDOM_LOC])
    return image_to_base64(selected_res)


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
        print(type(data))
        return data


class ImageSearchService(image_search_pb2_grpc.ImageSearchServiceServicer):

    def SearchImage(self, request, context):
        keyword = request.keyword
        image_base64 = search_files(keyword)
        return image_search_pb2.SearchResponse(image_str=image_base64)


def serve():
    print(f"Listening in port {50051}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_search_pb2_grpc.add_ImageSearchServiceServicer_to_server(
        ImageSearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()