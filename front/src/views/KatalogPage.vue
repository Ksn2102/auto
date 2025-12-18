<template>
    <div class="vmeste">
        <div class="conteiner15">
            <div class="first">
                <div>
                    <h1 class="filtrs1">Цена</h1>
                    <div class="mini">
                        <div class="centerrr9">
                            <label for="username">От</label>
                            <input type="text" class="ramka">
                        </div>
                        <div class="centerrr9">
                            <label for="username">До</label>
                            <input type="text" class="ramka">
                        </div>
                    </div>
                    <h1 class="filtrs">Категория</h1>
                    <div class="filtrs">
                        <select class="my">
                            <option selected="" value="volvo">Все</option>
                            <option value="volvo">Седан</option>
                            <option value="saab">Внедорожник</option>
                            <option value="vw">Кроссовер</option>
                        </select>
                    </div>
                    <div class="filtrs2">
                        <div class="center9">
                            <input type="checkbox">
                            <label for="username">Год</label>
                        </div>
                        <div class="center9">
                            <input type="checkbox">
                            <label for="username">Наименование</label>
                        </div>
                        <div class="center9">
                            <input type="checkbox">
                            <label for="username">Цена</label>
                        </div>
                    </div>
                    <p class="filtrs"><button class="search">Искать</button></p>
                </div>
            </div>
            <div class="second">
                <h1 class="filtrs1">Наш ассортимент</h1>
                <div class="one1">
                     <div 
                        class="pervoe1"
                        v-for="car in cars"
                        :key="car.id"
                     >
                        <p class="photo">
                            <img class="razmer12"
                            :src="require(`@/assets/${car.img}`)"
                            />
                        </p>
                        <p class="opic">{{ car.text }}</p>
                        <p class="opic">{{ car.price }}</p>
                        <p class="photo">
                            <router-link :to="`/katalog/${car.id}`" class="pp">Подробнее</router-link>
                        </p>
                     </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import cars from "@/mocks/cars.json"
export default {
    name: 'KatalogPage',
    data() {
        return {
            cars: cars
        }
    }
};
</script>
<style>
@import '@/styles/katalog.css';
label{
text-align: center;
}   

.mini{
    display: flex;
    gap: 20px;
}

.second{
    padding-bottom: 20px;
    margin-left: 100px;
}

.flex {
    display: flex;
    justify-content: center;
    gap: 60px;
    align-items: center;
}

a{
    color: inherit;
    text-decoration: none;
}

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
    border: none;
    background-color: #2947bc78;
    border-radius: 20px;
    border: 1px solid #000000;
}

.pp{
    padding: 3px 10px;
    margin: 10px;
    border: none;
    background-color: #2947bc78;
    border-radius: 20px;
    border: 1px solid #000000;
}

.logo{
    width: 90px;
}

.zagolovok{
    padding-top: 30px;
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
    font-size: 25px;
}

.filtrs1{
    text-align: center;
    padding-top: 50px;
    font-size: 25px;
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
    margin: 5px 0 10px;
}

.pervoe {
    position: relative;
    overflow: hidden;
}

.pervoe1{
    border: 2px solid rgb(0, 0, 0);
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
    padding: 5px;
    width: calc((100% / 3) - 34px)
}

@media (max-width: 1024px) {
    .pervoe1 {
        width: calc((100% / 2) - 34px)
    }
}

.one1{
    display: flex;
    gap: 30px;
    padding-top: 10px;
    flex-wrap: wrap;
}

.one2{
    display: flex;
    gap: 30px;
    margin-top: 20px;
}

.razmer12{
    width: 270px;
    height: 250px;
}

.conteiner15 {
    max-width: 1300px;
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    flex: auto 1;
}

.ramka{
    width: 50px;
    border-radius: 20px;
    border: 1px solid #255aba;
}

.my{
    border-radius: 20px;
    border: 1px solid #255aba;
}

.center9{
    display: flex;
}

.centerrr9x{
    display: flex;
    padding: 10px;
}

.flex2{
    display: flex;
    margin-top: 20px;
    justify-content: space-around;
}

.dop{
    border-bottom: 1px solid black;
}

.podrobno{
    margin-top: 30px;
}

.centerr{
    text-align: center;
    padding: 5px 30px;
    margin-top: 15px;
}

@media (max-width: 768px) {
    .conteiner15 {
        flex-direction: column; 
        display: block;
    }

    .first {
        max-width: 100%; 
        margin-bottom: 20px;
    }

    .second {
        max-width: 100%; 
    }

    .centerrr9x{
        justify-content: center;
    }

    .center9{
        justify-content: center;
    }
}

@media (max-width: 480px) {
    .filtrs, .filtrs1 {
        font-size: 20px; 
    }

    .ramka, .my {
        width: 100%; 
    }

    .search, .pp {
        width: 100%; 
        padding: 10px;
    }
}

@media (max-width: 320px) {
    .filtrs, .filtrs1 {
        font-size: 20px; 
    }

    .ramka, .my {
        width: 100%;
    }

    .search, .pp {
        width: 100%;
        padding: 10px;
    }

    .pervoe1 {
        width:100%;
    }

    
    .centerrr9{
        justify-content: center;
    }

    .center9{
        justify-content: center;
    }
}
</style>