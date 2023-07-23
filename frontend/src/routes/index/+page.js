export async function load({ fetch }) {

    let all = await fetch('http://127.0.0.1:8000/api/itfcd/count');
    let booksen = await fetch('http://127.0.0.1:8000/api/complete/booksen/status/10/count');
    let product = await fetch('http://127.0.0.1:8000/api/complete/product/status/10/count');
    let image = await fetch('http://127.0.0.1:8000/api/complete/image/status/10/count');
    let weight = await fetch('http://127.0.0.1:8000/api/complete/weight/status/10/count');
    let price = await fetch('http://127.0.0.1:8000/api/complete/price/status/10/count');
    let stock = await fetch('http://127.0.0.1:8000/api/complete/stock/status/10/count');
    let variant = await fetch('http://127.0.0.1:8000/api/complete/variant/status/10/count');

    let all_cnt = await all.json()

    return {
        all_cnt : all_cnt,
        cnt : [
            {name:'all', count:all_cnt},
            {name:'booksen', count:await booksen.json()},
            {name:'product', count:await product.json()},
            {name:'image', count:await image.json()},
            {name:'weight', count:await weight.json()},
            {name:'price', count:await price.json()},
            {name:'stock', count:await stock.json()},
            {name:'variant', count:await variant.json()},
        ],
    };
    //결과 뱉어내기
}