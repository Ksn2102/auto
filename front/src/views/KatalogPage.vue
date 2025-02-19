<template>
    <div class="vmeste">
        <div class="conteiner15">
            <div class="first">
                <div>
                    <h1 class="filtrs1">Цена</h1>
                    <div>
                        <div class="centerrr">
                            <label for="username">От</label>
                            <input type="text" class="ramka">
                        </div>
                        <div class="centerrr">
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
                        <div class="center">
                            <input type="checkbox">
                            <label for="username">Год производства</label>
                        </div>
                        <div class="center">
                            <input type="checkbox">
                            <label for="username">Наименование</label>
                        </div>
                        <div class="center">
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
                    <!-- <a href="../pages/product.html"> </a>-->
                     <div 
                        class="pervoe1"
                        v-for="car in cars"
                        :key="car.id"
                     >
                        <p class="photo">
                            <img class="razmer1"
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
.second{
    padding-bottom: 20px;
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

.razmer{
    width: 200px;
    height: 150px;
}

.razmer1{
    width: 200px;
    height: 250px;
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

.razmer1{
    width: 330px;
    height: 250px;
}

/* .razmer2{
    width: 290px;
    height: 250px;
}

.razmer3{
    width: 200px;
    height: 150px;
    margin-left: 45px;
} */

.conteiner15 {
    max-width: 1300px;
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    flex: auto 1;
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

.center{
    display: flex;
}

.centerrr{
    display: flex;
    padding: 10px;
}
/*Товар*/
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
</style>