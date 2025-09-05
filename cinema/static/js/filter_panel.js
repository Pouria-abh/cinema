function subfilter(){
    filter=$('#filter-op').val();
    $.get('/gener/'+filter).then(res=>{
        console.log(res);
    $('#filter-op').val();
    });
}