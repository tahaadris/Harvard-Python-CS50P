file_name = input("File name: ").lower().strip() 

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")





# match file_name:
#     case file_name.endswith(".gif"):
#         print("imange/gif")
#     case ".jpg" | ".jpeg":
#         print("image/jpeg")
#     case ".png" : 
#         print("image/png")
#     case ".pdf":
#         print("application/pdf")
#     case ".txt":
#         print("text/plain")
#     case ".zip":
#         print("application/zip")
#     case _:
#         print("application/octet-stream")