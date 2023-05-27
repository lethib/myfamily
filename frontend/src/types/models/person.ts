export type Person = {
    id: number
    first_name: string
    last_name: string
    gender: 'M' | 'F' | 'U'
    date_birth: string
    date_death: string | null
}