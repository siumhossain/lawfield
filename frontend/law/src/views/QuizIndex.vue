<template >
    <div>
        <div class="conatiner">
            <div class="row my-5 mx-2">
                <i @click="back()" class="fas fa-long-arrow-alt-left"> Back</i>
                
            </div>

        </div>
        
       <div class="group">
            <h4 class="mx-2 my-3">How many question do you want?</h4>
            <button @click="for5()" class="btn btn-primary">5</button>
            <button @click="for10()" class="btn btn-primary mx-2">10</button>
            <button @click="for15()" class="btn btn-primary">15</button>
        </div>
    </div>
</template>
<script>
export default {
    name:'QuizIndex',
    methods:{
        back(){
            this.$router.go(-1)
        },
        for5(){
            console.log('5')
            this.$router.push({
                name:'quiz',
                params:{
                    q:'5'
                }
            })
        },
        for10(){
            console.log('10')
            this.$router.push({
                name:'quiz',
                params:{
                    q:'10'
                }
            })
        },
        for15(){
            console.log('15')
            this.$router.push({
                name:'quiz',
                params:{
                    q:'15'
                }
            })
        }
    },
}
</script>
<style>
.group {
  position:relative;
  text-align:center;
  white-space: nowrap;                 /*  make buttons stay on 1 line  */
  left: 50%;                           /*  position its left edge in the middle  */
  top: 30vh;                           /*  position its top edge in the middle */
  transform: translate(-50%,-50%);     /*  move left/top back half its own width/height  */
}
</style>