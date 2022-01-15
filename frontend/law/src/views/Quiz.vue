<template >
    <div>
        <div class="row">
            <div class="row mt-3 mb-3 mx-2">
                <i @click="back()" class="fas fa-long-arrow-alt-left"> Back</i>
                
            </div>
        </div>
              <div class="row mt-5">
           <div class="col">
               <div class="container">
                   <div v-for="i in obj" :key="i.id"  class="list-group mb-4">
                        <button
                            type="button"
                            class="list-group-item list-group-item-action active"
                            aria-current="true"
                        >
                            {{i.question}}
                        </button>
                        <button type="button"
                        @click="ansCheck(i.id,i.option_A)"
                        class="list-group-item list-group-item-action">
                            {{i.option_A}}
                        </button>
                        <button type="button"
                        @click="ansCheck(i.id,i.option_B)"
                         class="list-group-item list-group-item-action">
                            {{i.option_B}}
                        </button>
                        <button type="button" 
                        @click="ansCheck(i.id,i.option_C)"
                        class="list-group-item list-group-item-action">
                            {{i.option_C}}
                        </button>
                        <button type="button"
                        @click="ansCheck(i.id,i.option_D)"
                         class="list-group-item list-group-item-action">
                            {{i.option_D}}
                        </button>

                        <div v-if='welcome && i.id === selected_obj_id' class="card">
                           <div v-if='ans' class="card-body right"
                          
                           >
                           <b>{{rightAns}}</b> is right ans <br>
                               🎉🎉 You are absolutely correct 🎉🎉<br>
                               
                               
                           </div>
                           <div v-if="ans === false" class="card-body wrong">
                               Sorry, your ans is incorrect <br>
                               Right ans is <b>{{rightAns}}</b>

                           </div>
                
                        </div>

                        
                        </div>
               
                </div>

           </div>
           
       </div>
        
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Quiz',
    data(){
        return{
            obj:[],
            rightAns:'',
            welcome:false,
            ans:false,
            selected_obj_id:''
            
        }
    },
    methods:{
        ansCheck(id,ans){
            delete  axios.defaults.headers.common["Authorization"];
            axios.get(`api/quiz/ans/${id}/`)
            .then(res => {
                console.log(res.data['right_ans'])
                this.rightAns = res.data['right_ans']
                this.selected_obj_id = id
                if(this.rightAns === ans){
                    this.welcome = true
                    this.ans = true
                }
                else{
                    this.welcome = true
                    this.ans = false
                }

                
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
            })
            
            
        },
        back(){
            this.$router.go(-1)
        }
    },
    async created(){
        delete  axios.defaults.headers.common["Authorization"];
        const q = this.$route.params.q
        console.log(q)
        await axios.get(`api/quiz/${q}/`)
        .then(res => {
            this.obj = res.data
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
        })
        .then(err => {
            console.log(err)
        })

    }
}
</script>
<style scoped>
.right{
    border: solid;
    border-color: #06FF00;
}
.wrong{
    border: solid;
    border-color:crimson;
}
</style>