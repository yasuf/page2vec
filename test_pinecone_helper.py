import unittest
from unittest.mock import Mock, patch, MagicMock
from io import StringIO
from pinecone_helper import upload_file_to_pinecone

class TestPineconeHelper(unittest.TestCase):

    @patch('pinecone_helper.Pinecone')
    def test_upload_file_to_pinecone_basic(self, mock_pinecone):
        """Test basic functionality of upload_file_to_pinecone"""
        # Setup mock objects
        mock_pc = Mock()
        mock_index = Mock()
        mock_pinecone.return_value = mock_pc
        mock_pc.Index.return_value = mock_index

        # Create test file content
        test_content = "line 1\nline 2\nline 3\n"
        test_file = StringIO(test_content)

        # Test parameters
        api_key = "test_api_key"
        index_name = "test_index"
        namespace = "test_namespace"

        # Call the function
        upload_file_to_pinecone(
            file=test_file,
            pinecone_api_key=api_key,
            pinecone_index=index_name,
            pinecone_namespace=namespace
        )

        # Verify Pinecone was initialized with correct API key
        mock_pinecone.assert_called_once_with(api_key=api_key)

        # Verify index was accessed
        mock_pc.Index.assert_called_once_with(index_name)

        # Verify upsert_records was called
        mock_index.upsert_records.assert_called()

        # Check that the correct number of records were processed
        call_args = mock_index.upsert_records.call_args[0]
        self.assertEqual(call_args[0], namespace)  # namespace
        batch_data = call_args[1]  # batch data
        self.assertEqual(len(batch_data), 3)  # 3 lines

        # Verify record structure
        expected_records = [
            {"_id": "rec1", "text": "line 1\n"},
            {"_id": "rec2", "text": "line 2\n"},
            {"_id": "rec3", "text": "line 3\n"}
        ]
        self.assertEqual(batch_data, expected_records)


if __name__ == '__main__':
    unittest.main()
