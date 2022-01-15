<template>
  
    
    <div class="container mt-5">
      <div class="row my-3">
        <div class="col-sm-5">
          <b class="display-4">About us</b>
          <p class="display-7 my-2">{{$store.state.about.description}}</p>
          <button @click="searchLaw()" class="btn btn-primary ">Search Law</button>
          <button @click="team()" class="btn btn-primary mx-2">Meet our team</button>
          

        </div>
        
      </div>
    </div>
    
    
    
  
  <router-view></router-view>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src


export default {
  name: 'Home',
  
  async created(){
    
    delete  axios.defaults.headers.common["Authorization"];
    axios.get('api/about/')
    .then(res => {
      const about = res.data[0]
      //console.log(res.data[0])
      axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')

      this.$store.dispatch('about',about)
      console.log(this.$store.state.about)
    })
  },
  methods:{
    team(){
      this.$router.push('/team')
    },
    searchLaw(){
      this.$router.push('/searchLaw')
    }
  }
  
}
</script>
<style>
.display-5{
  font-weight: 800;
  }
.btn a{
  color:white
}
</style>