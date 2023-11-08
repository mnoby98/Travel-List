export default function Stats({ items }) {
  const numItems = items.length;
  const numPacked = items.filter((item) => item.packed).length;
  const percentage = Math.round((numPacked / numItems) * 100);
  return (
    <footer className="stats">
      <em>
        {percentage === 100
          ? "You got everything ~ Ready to go ✈ "
          : `You have ${numItems} items on your list,and you already packed ${numItems} (${percentage}%)`}
      </em>
    </footer>
  );
}
