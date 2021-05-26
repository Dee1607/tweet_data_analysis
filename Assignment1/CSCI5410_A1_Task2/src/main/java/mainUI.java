
public class mainUI {

	public static void main(String args[]) {

		// File upload on existing bucket
		String filePath = "/Users/deeppatel/Desktop/Task-2/Deep.txt";
		UploadFile objUpload = new UploadFile();
		objUpload.uploadFileToS3Bucket(filePath);

		// Bucket creation using Java,
		// Updating permissions of bucket using java and
		// Providing Full Control Using ACL in Java
		CreateBucket objCreate = new CreateBucket();
		objCreate.create_S3_Bucket();
		objCreate.updatePermissions();
		objCreate.setFullControlToUserUsingACL();

		// Move Files from 1st bucket to 2nd bucket
		MoveFiles objMoveFiles = new MoveFiles();
		objMoveFiles.moveFilesBetweenBuckets();
	}
}