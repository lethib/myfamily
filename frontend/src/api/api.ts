import axios, { AxiosError, AxiosResponse, AxiosInstance } from 'axios'

class Api {
    baseURL: string;
    client: AxiosInstance;

    constructor(baseURL: string) {
        this.baseURL = baseURL;
        this.client = axios.create({baseURL})

        this.client.interceptors.response.use(
            (response: AxiosResponse) => response,
            (error: AxiosError) => {
                const { data: errorData } = error.response!;
                console.error(errorData)
            }
        )
    }

    get = async <T>(path: string): Promise<T> => {
        const result = await this.client.get<T>(path)
        return result.data
    }
}

export const familyApiInstance = new Api('http://localhost:8000')