<template>
    <div>
        <div>
            <h1>My Test</h1>
            <button type="button" style="height:20px ; width:150px">{{my_data}}</button>
            <h1>My Test22</h1>
            <button type="button" style="height:20px ; width:150px">{{my_data2}}</button>
            <hr>
            <h1>임직원 리뷰분석 요청</h1>
            <h5>{{review}}</h5>
            <!-- <h1>{{review}}</h1>             -->
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return {
            my_data :'',
            my_data2 : '',
            // 긍부정도 리뷰 요청값
            review : '',
        }
    },
    methods: {
        getMyData(){
            // backend 주소로 가서 그 주소에서 return 해주는 값을 가져온다. 
            let path ="http://"+window.location.hostname+":5000/";
            axios.get(path).then((res)=>{
                this.my_data = res.data;
            }).catch((error) =>{
                console.error(error);
            });


            let path2 ="http://"+window.location.hostname+":5000/health_check";
            axios.get(path2).then((res)=>{
                this.my_data2 = res.data;
            }).catch((error) =>{
                console.error(error);
            });

            let path3 ="http://"+window.location.hostname+":5000/review";
            axios.get(path3).then((res)=>{
                this.review = res.data;
            }).catch((error) =>{
                console.error(error);
            });


        },
        
    },
    created() {
            this.getMyData();
    },
}
</script>

<style>

</style>