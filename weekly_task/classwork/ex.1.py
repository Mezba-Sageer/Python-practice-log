#Question 1: Classify Each File as Image or Document
# Question:
# Given a list of file names, print each file name along with its type: either Image or Document.
# Image files: .jpg, .jpeg, .png, .gif
# Document files: .pdf, .docx, .txt

# Example Input:
# files = ["photo1.jpg", "report.pdf", "image.png", "notes.txt",
#     "logo.gif", "resume.docx", "holiday.jpeg", "data.csv"]

# Expected Output:
# photo1.jpg - Image
# report.pdf - Document
# image.png - Image
# notes.txt - Document
# logo.gif - Image
# resume.docx - Document
# holiday.jpeg - Image
# data.csv - Unknown

files=["photo1.jpg", "report.pdf", "image.png", "notes.txt","logo.gif", "resume.docx", "holiday.jpeg", "data.csv"]
image_files=[ '.jpg','.jpeg','.png','.gif']
doc_files=['.pdf','.docx','.txt']
for i in range(len(files)):
    for j in image_files:
        if(j in files[i]):
            print(files[i],"-","Image")
    for k in doc_files:
        if(k in files[i]):
            print(files[i],"-","Document")


