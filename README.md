# Searchable PDF Flask Server

By Kamden Wilson

**Searchable PDF Flask Server** is a server built with flask that receives a pdf from a client and returns a searchable pdf. It uses the
[pytesseract wrapper](https://github.com/madmaze/pytesseract) for the [tesseract OCR](https://github.com/tesseract-ocr/tesseract) to process
pfds.

Features
- [ ] **API method for receiving and returning pdfs to client**
- [ ] **python function that converts a pdf into a searchable pdf through pytesseract**

Future Optional Features:
- [ ] **Server can receive multiple pdfs from one user and return multiple pdfs**
- [ ] **Server can receive and process images like png and jpg**
- [ ] **Make OCR faster**
- [ ] **Update client on pdf processing duration**
- [ ] **Handle server receiving non-compatible file types**

# Known issues
Pytesseract is very slow because it uses tesseract executable to process images. The executable has to be run once per image rather than running it one time and giving it
every image at once. One solution could be to use a different tesseract wrapper that would let me give it all images at once for processing. Another would be to use multiple
threads to process images simultaneously.

There is no error handling if a client sends the server a file that isn't a pdf. The client does not receive any feedback on the status of the pdf processing so it just has to wait
for a response or error.

## License

    Copyright 2023 Kamden Wilson

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
