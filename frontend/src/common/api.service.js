import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import { API_URL } from "@/common/config";

const ApiService = {
    init() {
        Vue.use(VueAxios, axios);
        Vue.axios.defaults.baseURL = API_URL;
    },
    query(resource, params) {
        return Vue.axios.get(resource, params).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },
    get(resource, slug = "") {
        return Vue.axios.get(`${resource}/${slug}`).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },
    post(resource, params) {
        return Vue.axios.post(`${resource}`, params);
    },
    delete(resource) {
        return Vue.axios.delete(resource).catch(error => {
            throw new Error(`[RWV] ApiService ${error}`);
        });
    },
    update(resource, slug, params) {
        return Vue.axios.put(`${resource}/${slug}`, params.favorite);
    },
};


export default ApiService;

export const FavoriteService = {
    query(type, params) {
        return ApiService.query("favorites" + (type === "feed" ? "/feed" : ""), {
            params: params
        });
    },
    get(slug) {
        return ApiService.get("favorites", slug);
    },
    create(params) {
        return ApiService.post("favorites", params );
    },
    destroy(slug) {
        return ApiService.delete(`favorites/${slug}`);
    },
    update(slug, params) {
        return ApiService.update("favorites", slug, { favorite: params });
    },
};

export const CategoriesService = {
    query(type, params) {
        return ApiService.query("categories", {
            params: params
        });
    },
    get(slug) {
        return ApiService.get("categories");
    },
    create(params) {
        return ApiService.post("categories", params );
    },
};