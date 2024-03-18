import pytest
import grpc
import image_search_pb2
import image_search_pb2_grpc


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return image_search_pb2_grpc.add_ImageSearchServiceServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    from image_search_pb2_grpc import ImageSearchService
    return ImageSearchService()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return image_search_pb2_grpc.ImageSearchServiceStub(grpc_channel)


def test_valid_request(grpc_stub):
    request = image_search_pb2.SearchRequest(keyword='cat')
    response = grpc_stub.SearchImage(request)
    assert response.image_str != ""  # Assuming the response should not be empty


def test_invalid_keyword(grpc_stub):
    request = image_search_pb2.SearchRequest(keyword='nonexistent')
    response = grpc_stub.SearchImage(request)
    assert response.image_str == ""  # Assuming an empty string for invalid keywords


def test_empty_keyword(grpc_stub):
    request = image_search_pb2.SearchRequest(keyword='')
    response = grpc_stub.SearchImage(request)
    assert response.image_str == ""  # Assuming an empty string for empty keywords


def test_large_keyword(grpc_stub):
    request = image_search_pb2.SearchRequest(keyword='a' * 1000)
    response = grpc_stub.SearchImage(request)
    assert response.image_str == "" 
    # Assuming handling or validation for keyword size, may expect an empty or specific response


def test_concurrency(grpc_stub):
    from concurrent.futures import ThreadPoolExecutor

    def make_request():
        request = image_search_pb2.SearchRequest(keyword='cat')
        return grpc_stub.SearchImage(request).image_str

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(make_request, range(10)))
    assert all(result != "" for result in results)  # Assuming all requests return valid responses
