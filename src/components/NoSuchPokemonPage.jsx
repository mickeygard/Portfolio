import { useParams } from "react-router-dom";

export default function NoSuchPokemonPage() {
  const { pokemonNameOrId } = useParams();

  return <div>No such pokemon with name or id '{pokemonNameOrId}' exists!</div>;
}