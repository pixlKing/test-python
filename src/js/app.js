function getfolder(e) {
    var files = e.target.files;
    var path = files[0].webkitRelativePath;
    var Folder = path.split("/");
    //alert(Folder[0]);
    console.log(e.target);
}