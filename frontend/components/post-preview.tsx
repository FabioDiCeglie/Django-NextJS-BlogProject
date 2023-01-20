import Link from "next/link";
import Avatar from "./avatar";
import CoverImage from "./cover-image";
import DateFormatter from "./date-formatter";
import Post from "../interfaces/post";

type Props = {
  article: Post;
};

const PostPreview = ({ article }: Props) => {
  const { title, coverImage, date, author_name, author_picture, id } = article;
  return (
    <div>
      <div className="mb-5">
        <CoverImage id={id} title={title} src={coverImage} />
      </div>
      <h3 className="text-3xl mb-3 leading-snug">
        <Link
          as={`/posts/${id}`}
          href="/posts/[id]"
          className="hover:underline"
        >
          {title}
        </Link>
      </h3>
      <div className="text-lg mb-4">
        <DateFormatter dateString={date} />
      </div>
      <Avatar name={author_name} picture={author_picture} />
    </div>
  );
};

export default PostPreview;
