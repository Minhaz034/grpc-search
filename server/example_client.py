import grpc
import base64
import image_search_pb2
import image_search_pb2_grpc

def search_image(keyword):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_search_pb2_grpc.ImageSearchServiceStub(channel)
        request = image_search_pb2.SearchRequest(keyword=keyword)
        response = stub.SearchImage(request)
        return response

if __name__ == "__main__":
    keyword = "cat"
    response = search_image(keyword)
    print(f"Received image data for keyword '{keyword}'.")

    # Example for decoding base64 image data
    image_data = base64.b64decode(response.image_str)
    with open('received_image.jpg', 'wb') as image_file:
        image_file.write(image_data)
