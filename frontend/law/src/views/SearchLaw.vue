<template >
    <div>

    

    <div class="row text-center mx-3 mt-5">
        <button @click="quiz()" class="btn btn-primary">Want to play quiz game</button>
    </div>
    <div class="container mt-3">
        
            <input v-model='search' class="form-control" type="text" placeholder="🔍 Search">
        
    </div>
    
    <div class="row mx-2">
        <div class="container mt-3 ">
        <ul v-for="law in laws" :key="law.id" class="list-group">
            <li class="list-group-item shadow-5 mb-3">

                <router-link :to="{name:'DetailsLaw',params:{id:law.id}}">
                     <h5>{{law.act_no}}</h5>
                </router-link>
               
                {{law.title}} <br>
                Date: {{law.date}}
                <hr>
                <h5>Description</h5>
                <span v-html="law.description"></span>
            </li>
 
        </ul>
    
    </div>
    <router-view></router-view>
    </div>
    
    </div>
    
</template>
<script>
import axios from 'axios'
export default {
    name:'SearchLaw',
    data(){
        return{
            laws:[],
            search:''
        }
    },
    methods:{
        quiz(){
            this.$router.push('/quizIndex')
        }
    },
    created(){
        delete  axios.defaults.headers.common["Authorization"];
        axios.get('api/law/')
        .then(res => {
            console.log(res.data)
            this.laws = res.data
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
        })
    },
    watch: {
        search(v){
            console.log(v)
            const data = {
                value:v
            }
            delete  axios.defaults.headers.common["Authorization"];
            axios.post('api/lawSearch/',data)
            .then(res => {
                console.log(res.data)
                this.laws = res.data
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
            })
            

        }
    }
}
</script>
<style >
    
</style>