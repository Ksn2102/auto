<template>
        <div class="conteiner19" v-if="car">
            <p class="zagolovok">{{ car.text }}</p>
            <div class="flex2">
                <img class="pic" :src="require(`@/assets/${car.img}`)"/>
                <div>
                    <p>Цвет:{{ car.color }}</p>
                    <p>Габариты:3 x 3 x 4 м</p>
                    <p>Масса:{{ car.weight }}</p>
                    <h1>{{ car.price }}</h1>
                    <p class="photo"><button class="centerr">Договориться о встрече</button></p>
                </div>
            </div>
            <div class="podrobno">
                <p class="dop">Описание</p>
                <p>{{ car.opic }}</p>
            </div>
        </div>
</template>
<script>
import cars from '@/mocks/cars.json';
export default {
    name: 'IndividPage',
    data() {
        return {
            car: null,
        }
    },
    computed: {

    },
    mounted() {
        this.car = cars.find(car => car.id === +this.$route.params.id)
    }
};
</script>
<style>


a{
    color: inherit;
    text-decoration: none;
}

/* button{
    border: none;
    background-color: #40E0D0;
    border: 1px solid #244e24;
} */

.rasstoyanie{
    gap: 95px;
}

.rego{
    padding: 10px;
}

.otstopp{
    margin-left: 15px;
    padding: 10px 25px;
}

.search{
    padding: 5px 25px;
}

.pp{
    padding: 3px 10px;
    margin: 10px;
}

.logo{
    width: 90px;
}

.zagolovok{
    padding-top: 30px;
    font-weight: bolder;
}

.vmeste{
    display: flex;
}

.nal{
    display: flex;
    gap: 9px;
    justify-content: center;
    padding-top: 10px;
}

.filtrs{
    text-align: center;
    padding-top: 10px;
}

.filtrs1{
    text-align: center;
    padding-top: 50px;
}

.filtrs2{
    padding-top: 10px;
}

.one{
    display: flex;
    justify-content: space-evenly;
}


.opic{
    text-align: center;
}

.opic1{
    text-align: center;
    color: red;
}

.pervoe{
    border: thick double rgba(201, 177, 158, 0.222);
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
}

.photo{
    text-align: center;
}

.pervoe {
    position: relative;
    overflow: hidden;
}

.pervoe img {
    transition: transform 0.3s ease;
}

.one1{
    display: flex;
    gap: 30px;
    padding-top: 10px;
}

.one2{
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}



.conteiner19 {
    max-width: 1000px;
    width: 100%;
    margin: 0 auto;
    padding-bottom: 60px;
}

.ramka{
    width: 100px;
    border-radius: 20px;
    border: 1px solid #255aba;
}

.my{
    border-radius: 20px;
    border: 1px solid #255aba;
}
/*Товар*/
.flex2{
    display: flex;
    margin-top: 20px;
    justify-content: space-evenly;
}

.dop{
    border-bottom: 1px solid black;
    font-weight: bolder;
}

.podrobno{
    margin-top: 30px;
}

.centerr{
    text-align: center;
    padding: 5px 30px;
    margin-top: 15px;
    background: #7689bc;
    border: 1px solid;
    color: black;
    border-radius: 15px;
}

.pic{
    width: 300px;
}

</style>