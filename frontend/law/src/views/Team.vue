<template>
    <div class="row">
        
        <div class="container center text-center">
        <h2 class="my-3">Our Team</h2>
        </div>
    </div>

    <div class="row text-center mx-2">
        <p>
            Our team is made up of dedicated and talented individuals from diverse backgrounds, who combine the ability to deliver local knowledge with an experience of international business.
        </p>

    </div>
    
    <div class="container mb-3">
        <div class="input-group mb-3">
            
            <select v-model="selected" >
                <option  disabled value="">Search By</option>
                <option>Name</option>
                <option>Category</option>
                <option>Position</option>

                <option>Area</option>
            
            </select>
            
              <input v-model="searchValue" type="text" placeholder="Type..." class="form-control" aria-label="Text input with dropdown button" />

        </div>
    </div>
    

        
    
  
    

    <!-- for search category-->
    <!-- <div  class="container">
        <div class="row">
            <div class="col">
                <form>
                    <div class="mb-3">
                        
                        <input type="text" class="form-control" placeholder='Search...' required>
                    </div>
                </form>
            </div>
            
            
        </div>
    </div> -->
   
            
          
    
    <div class="container">
         <div v-for="i in lawyer" :key="i.id" class="card mb-3 mx-2 my-3 shadow-5" style="max-width: 540px;">
        <div class="row no-gutters">
            <div class="col">
            <img src="../assets/avatar.jpg" class="card-img" >
            </div>
            <div class="col">
            <div class="card-body mt-2 d-flex flex-column ">
                <h3 class="card-title">{{i.name}}</h3>
                <small>{{i.category}}</small>
                <!-- <small>{{i.id}}</small> -->
                <small>{{i.position}}</small>
                <br>
                <button @click="submit(i.id)" class="btn btn-primary">
                    Contact
                </button>
            </div>
            </div>
        </div>
    </div>
        
    </div>
    
    <router-view></router-view>
    
</template>
<script>
import axios from 'axios'

export default {

    

    data(){
        return{
            position_value:'',
            position:{},
            search_value:'',
            lawyer:{},
            category:false,
            name:false,
            selected:'',
            searchValue:''
        }
    },

    watch:{
        searchValue: async function(value){
            
            
            if(this.selected === "Name"){
                await axios.get(`api/lawyer_name/${value}/`)
                .then(res => {
                    console.log(res.data)
                    this.lawyer = res.data
                })
            }
            else if(this.selected === "Category"){
                await axios.get(`api/lawyer_category/${value}/`)
                .then(res => {
                    console.log(res.data)
                    this.lawyer = res.data
                })
            }
            else if(this.selected === "Position"){
                await axios.get(`api/lawyer_position/${value}/`)
                .then(res => {
                    console.log(res.data)
                    this.lawyer = res.data
                })
            }
            else if(this.selected === "Area"){
                await axios.get(`api/lawyer_area/${value}/`)
                .then(res => {
                    console.log(res.data)
                    this.lawyer = res.data
                })
            }
            
            
        }
        

    },

  
    
    async created() {
        delete  axios.defaults.headers.common
        await axios.get('api/position/')
        .then(res => {
            this.position = res.data
            
            console.log('done')
            axios.get('api/all-lawyer/')
            .then(res => {
                
                this.lawyer = res.data
                console.log(this.lawyer)
            })

            
            
        })
        
       
    },
    methods:{
        category: function(){
            console.log('category click')
            
        },
        name: function(){
            console.log('name_click')
        },
        submit(id){
            console.log(id)
            this.$router.push({
                name:'Appointment',
                params:{
                    id:id
                }
            })

        },
    },
    
    
}
</script>
<style>
 .form-col{
     
     margin: 10px 30px;
     width: 300px;
 }   


</style>