// import logo from './logo.svg';
import './App.css';
import 'react-dropzone-uploader/dist/styles.css'
import Dropzone from 'react-dropzone-uploader'

function App() {
  return (
    <div className="App">
      {/* <MyUploader /> */}
      <Standard />
    </div>
  );
}

// return { url: 'https://httpbin.org/post' 
const Standard = () => {
  const getUploadParams = () => {
    // return { url: 'http://127.0.0.1:8000/fileUpload' 
    // }
    return {
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Host": "httpbin.org",
        "Postman-Token": "8083fc61-16e5-4c5a-9655-edd8d798f47d",
        "User-Agent": "PostmanRuntime/7.29.0",
        "X-Amzn-Trace-Id": "Root=1-621dd7f8-5c2d84177c78851476839386"
    },
    "json": null,
    "origin": "103.19.128.58",
    "url": "https://httpbin.org/post"
}
  }

  const handleChangeStatus = ({ meta }, status) => {
    // console.log(status, meta)
  }

  const handleSubmit = (files, allFiles) => {
    console.log(files.map(f => f.meta))
    uploadFile(files)
    // allFiles.forEach(f => f.remove())
  }

function uploadFile(files) {
  
  var formData = new FormData();
  
  files.map((file, index) => {
    formData.append(`file${index}`, file);
  });
  
  fetch('http://127.0.0.1:8000/fileUpload', {
    // content-type header should not be specified!
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(success => {
      // Do something with the successful response
    })
    .catch(error => console.log(error)
  );
}

  return (
    <div>
      <h1>Upload your fils heare </h1>
    <Dropzone
      getUploadParams={getUploadParams}
      onChangeStatus={handleChangeStatus}
      onSubmit={handleSubmit}
      styles={
          {
           dropzone: { minHeight: 500 ,width:1000},
          }
    }
    />
    </div>
  )
}


// const MyUploader = () => {
//   // specify upload params and url for your files
//   const getUploadParams = ({ meta }) => { return { url: 'https://httpbin.org/post' } }
  
//   // called every time a file's `status` changes
//   const handleChangeStatus = ({ meta, file }, status) => { console.log(status, meta, file) }
  
//   // receives array of files that are done uploading when submit button is clicked
//   const handleSubmit = (files) => { console.log(files.map(f => f.meta)) }

//   return (
//     <Dropzone
//       getUploadParams={getUploadParams}
//       onChangeStatus={handleChangeStatus}
//       onSubmit={handleSubmit}
//       accept="image/*,audio/*,video/*"
//     />
//   )
// }
export default App;
